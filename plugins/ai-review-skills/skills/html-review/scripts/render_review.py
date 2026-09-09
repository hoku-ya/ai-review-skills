#!/usr/bin/env python3
import hashlib,html,json,sys
from pathlib import Path
REQ=("schema_version","packet_id","title","canonical_inputs","summary","evidence","tests","audit")
CSS="body{font-family:system-ui;max-width:1000px;margin:auto;padding:2rem;background:#faf9f6;color:#171717}header,section,footer{background:white;border:1px solid #222;border-radius:10px;padding:1rem;margin:1rem 0}.critical{border-left:6px solid #b42318}code{overflow-wrap:anywhere}table{border-collapse:collapse;width:100%}th,td{border:1px solid #777;padding:.4rem;text-align:left}@media(max-width:600px){body{padding:.5rem}table{display:block;overflow:auto}}@media print{body{background:#fff}}"
def e(v): return html.escape("未提供" if v is None or v=="" else str(v),quote=True)
def table(items,fields):
 h="".join(f"<th>{e(x)}</th>" for x in fields); b=""
 for item in items:
  vals=[]
  for f in fields:
   v=item.get(f,"未提供"); v=json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v; vals.append(f"<td>{e(v)}</td>")
  b+="<tr>"+"".join(vals)+"</tr>"
 return f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"
def sec(title,body,cls=""): return f'<section class="{cls}"><h2>{e(title)}</h2>{body}</section>'
def main():
 src=Path(sys.argv[1]).read_bytes(); p=json.loads(src.decode()); missing=[x for x in REQ if x not in p]
 if missing or not p["canonical_inputs"]: raise ValueError("invalid Review Packet: "+str(missing))
 ids=[]
 for k in ("findings","evidence","tests","unresolved","human_decisions"): ids += [x.get("id") for x in p.get(k,[])]
 if len(ids)!=len(set(ids)): raise ValueError("IDs must be unique")
 evid={x["id"] for x in p["evidence"]}
 for f in p.get("findings",[]):
  if set(f.get("evidence_ids",[]))-evid: raise ValueError("dangling Evidence")
 if p["audit"].get("mode") not in ("parallel-subagents","sequential-single-agent"): raise ValueError("bad audit mode")
 s=p["summary"]; high=[x for x in p.get("findings",[]) if x.get("priority") in ("P0","P1") or x.get("status") in ("blocked","warning")]
 body=sec("Conclusion",f"<p>{e(s.get('status'))}: {e(s.get('conclusion'))}</p>")+sec("P0 / P1 / Blocked / Warning",table(high,["id","priority","status","title","claim","evidence_ids"]),"critical")+sec("Evidence",table(p["evidence"],["id","kind","locator","excerpt","verification","notes"]))+sec("Test results",table(p["tests"],["id","name","status","command","evidence_ids"]))+sec("Unresolved",table(p.get("unresolved",[]),["id","question","owner","blocking"]),"critical")+sec("Human Decision",table(p.get("human_decisions",[]),["id","question","options","status"]),"critical")+sec("Audit",f"<p>audit_mode: {e(p['audit'].get('mode'))}</p>"+table([p["audit"]],["checks","limitations"]))
 digest=hashlib.sha256(src).hexdigest(); inputs=table(p["canonical_inputs"],["kind","ref","sha256"])
 out=f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(p["title"])}</title><style>{CSS}</style></head><body><header>derived_snapshot | packet_id={e(p["packet_id"])} | source_sha256={digest}<h1>{e(p["title"])}</h1></header><main>{body}</main><footer><h2>Canonical inputs</h2>{inputs}<p>HTML is not the agent-to-agent source of truth.</p></footer></body></html>'
 Path(sys.argv[2]).write_text(out,encoding="utf-8")
if __name__=="__main__": main()
