import sys, docx
from docx.shared import Cm, Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d=docx.Document(sys.argv[1])
for s in d.sections:
    s.left_margin=s.right_margin=Cm(2.2); s.top_margin=s.bottom_margin=Cm(2)
for name in ['Normal','Body Text','First Paragraph','Compact']:
    try:
        st=d.styles[name]; st.font.size=Pt(10.5); pf=st.paragraph_format; pf.space_after=Pt(4); pf.space_before=Pt(0)
    except KeyError: pass
for name,sz in [('Heading 1',14),('Heading 2',12),('Title',18),('Subtitle',12)]:
    try:
        st=d.styles[name]; st.font.size=Pt(sz); st.paragraph_format.space_before=Pt(10); st.paragraph_format.space_after=Pt(4)
    except KeyError: pass
for t in d.tables:
    b=OxmlElement('w:tblBorders')
    for e in ['top','left','bottom','right','insideH','insideV']:
        x=OxmlElement('w:'+e); x.set(qn('w:val'),'single'); x.set(qn('w:sz'),'4'); x.set(qn('w:color'),'A0A0A0'); b.append(x)
    t._tbl.tblPr.append(b)
    for i,r in enumerate(t.rows):
        for c in r.cells:
            if i==0:
                sh=OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:fill'),'E8EEF4'); c._tc.get_or_add_tcPr().append(sh)
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(0)
                for run in p.runs:
                    run.font.size=Pt(9.5)
                    if i==0: run.bold=True
d.save(sys.argv[1])
