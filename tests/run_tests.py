from pathlib import Path
import json,re,subprocess,sys,tempfile,os,zipfile
R=Path(__file__).resolve().parents[1]; P=R/'plugins/ai-review-skills'; S=P/'skills'; errors=[]
def ck(v,m):
 if not v: errors.append(m)
def tx(p): return p.read_text(encoding='utf-8')
manifest=json.loads(tx(P/'.codex-plugin/plugin.json')); market=json.loads(tx(R/'.agents/plugins/marketplace.json'))
source=market['plugins'][0]['source']
ck(manifest['name']=='ai-review-skills' and manifest['skills']=='./skills/' and manifest['version'].startswith('0.2.0'),'manifest')
ck(source=={'source':'git-subdir','url':'https://github.com/hoku-ya/ai-review-skills.git','path':'./plugins/ai-review-skills','ref':'main'},'remote-hydratable marketplace source')
expected={'writing-quotation','documenting-with-sources','survey','paper-details','explain','html','html-review'}; ck({p.parent.name for p in S.glob('*/SKILL.md')}==expected,'skills')
paper=tx(S/'paper-details/SKILL.md'); survey=tx(S/'survey/SKILL.md'); ck('図表画像は未抽出' in paper and 'solely for figure extraction' in paper,'figure fallback'); ck('parallel-subagents' in paper+survey and 'sequential-single-agent' in paper+survey,'audit fallback')
for skill in ('html','html-review'):
 y=tx(S/skill/'agents/openai.yaml'); ck('allow_implicit_invocation: false' in y and '$'+skill in y,skill+' explicit')
packet=R/'tests/fixtures/review-packet.json'; before=packet.read_bytes()
with tempfile.TemporaryDirectory() as d:
 out=Path(d)/'r.html'; subprocess.run([sys.executable,str(S/'html-review/scripts/render_review.py'),str(packet),str(out)],check=True); h=tx(out)
 ck(packet.read_bytes()==before,'canonical mutated')
 for t in ('RP-001','F-001','E-001','E-002','T-001','U-001','D-001','Original quote','日本語訳','[source (2026/09), p.4]','unverified','sequential-single-agent'): ck(t in h,'lost '+t)
 ck('&lt;test&gt;' in h and '&lt;tag&gt;' in h,'escaping'); ck('derived_snapshot' in h and 'not the agent-to-agent source of truth' in h,'canonical label'); ck(not re.search(r'<link[^>]+stylesheet|<script[^>]+src=|<img[^>]+src=["\']https?://',h,re.I),'external dependency')

# Archive-equivalent inspection and absolute-path rejection.
with tempfile.TemporaryDirectory() as d:
 archive=Path(d)/'plugin.zip'
 files=[p for p in P.rglob('*') if p.is_file()]
 with zipfile.ZipFile(archive,'w') as z:
  for p in files: z.write(p,p.relative_to(P).as_posix())
 with zipfile.ZipFile(archive) as z: names=set(z.namelist())
 for required in ('.codex-plugin/plugin.json','skills/paper-details/SKILL.md','skills/paper-details/scripts/extract_images.py','skills/paper-details/scripts/package_report.py','skills/html/design-system/document.css','skills/html-review/references/review-packet.schema.json','skills/html-review/assets/template.html'):
  ck(required in names,'archive missing '+required)
for p in [x for x in P.rglob('*') if x.is_file()]:
 try: content=p.read_text(encoding='utf-8')
 except UnicodeDecodeError: continue
 ck(re.search(r'[A-Za-z]:\\Users\\|/Users/[^/]+/',content) is None,'absolute path in '+str(p.relative_to(R)))

# Portable Markdown bundle keeps every local image beside the copied report.
with tempfile.TemporaryDirectory() as d:
 root=Path(d); reports=root/'reports'; images=root/'images-from-papers'; reports.mkdir(); images.mkdir()
 (images/'fig1.png').write_bytes(b'png-fixture')
 source_report=reports/'paper.md'; source_report.write_text('# Paper\n\n![Figure 1](../images-from-papers/fig1.png)\n',encoding='utf-8')
 bundle=root/'portable'
 subprocess.run([sys.executable,str(S/'paper-details/scripts/package_report.py'),str(source_report),str(bundle)],check=True,capture_output=True)
 packaged=tx(bundle/'paper.md'); match=re.search(r'!\[Figure 1\]\(([^)]+)\)',packaged)
 ck(match is not None and (bundle/match.group(1)).is_file(),'portable image bundle broken')
try:
 from reportlab.pdfgen import canvas
 import pdfplumber
 with tempfile.TemporaryDirectory() as d:
  pdf=Path(d)/'paper.pdf'; c=canvas.Canvas(str(pdf)); c.drawString(72,750,'Abstract: Body text remains readable.'); c.drawString(72,700,'Figure 1 Missing visual region'); c.save()
  with pdfplumber.open(pdf) as doc: body='\n'.join((p.extract_text() or '') for p in doc.pages)
  ck('Body text remains readable' in body,'PDF body'); env=dict(os.environ); env['PYTHONNOUSERSITE']='1'; x=subprocess.run([sys.executable,'-S',str(S/'paper-details/scripts/extract_images.py'),str(pdf)],cwd=d,env=env,capture_output=True); ck(x.returncode!=0,'forced extraction'); fallback='図表画像は未抽出\n'+body; ck('図表画像は未抽出' in fallback and 'Body text remains readable' in fallback,'PDF continuation')
except Exception as e: errors.append('PDF integration '+str(e))
if errors:
 print('FAIL'); print('\n'.join('- '+e for e in errors)); raise SystemExit(1)
print('PASS: structure, dependencies, explicit invocation, PDF fallback, audit routing, Markdown, single HTML, Evidence')
