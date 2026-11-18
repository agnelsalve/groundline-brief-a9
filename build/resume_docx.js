// ATS resume as .docx (single column, real text, standard headings, subtle brand color)
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ExternalHyperlink, AlignmentType, LevelFormat,
  BorderStyle, TabStopType,
} = require("docx");

const ROOT = path.resolve(__dirname, "..");
const R = JSON.parse(fs.readFileSync(path.join(__dirname, "resume_content.json"), "utf8"));
const INK = "16141A", PLUM = "5B3A70", LINE = "DCD9E0";
const BODY = "Calibri", SERIF = "Georgia";
const SZ = 19; // 9.5pt
const RIGHT = 12240 - 2 * 792; // text width in DXA (0.55in margins)

const run = (text, o = {}) => new TextRun({ text, font: BODY, size: SZ, color: INK, ...o });
const heading = (t) => new Paragraph({
  children: [new TextRun({ text: t.toUpperCase(), font: BODY, size: 18, bold: true, color: PLUM, characterSpacing: 30 })],
  spacing: { before: 140, after: 50 }, keepNext: true,
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: LINE, space: 1 } },
});
const rowLine = (left, right) => new Paragraph({
  tabStops: [{ type: TabStopType.RIGHT, position: RIGHT }],
  spacing: { before: 50, after: 10 }, keepNext: true,
  children: [...left, ...(right ? [run("\t" + right)] : [])],
});
const bullet = (t) => new Paragraph({
  numbering: { reference: "b", level: 0 }, spacing: { after: 15, line: 250 },
  children: [run(t)],
});
const link = (text, url) => new ExternalHyperlink({ link: url, children: [run(text)] });

const c = R.contact;
const kids = [
  new Paragraph({ children: [new TextRun({ text: R.name, font: SERIF, size: 44, bold: true, color: INK })], spacing: { after: 20 } }),
  new Paragraph({ children: [run(R.title, { color: PLUM, size: 21, bold: true })], spacing: { after: 20 } }),
  new Paragraph({
    spacing: { after: 60 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: INK, space: 4 } },
    children: [
      run(`${c.location} | ${c.phone} | `), link(c.email, `mailto:${c.email}`), run(" | "),
      link(c.linkedin, `https://www.${c.linkedin}`), run(" | "), link(c.github, `https://${c.github}`),
    ],
  }),
  heading("Summary"),
  new Paragraph({ children: [run(R.summary)], spacing: { after: 20, line: 250 } }),
  heading("Technical Skills"),
  ...R.skills.map(([k, v]) => new Paragraph({ spacing: { after: 15, line: 250 }, children: [run(k + ": ", { bold: true }), run(v)] })),
  heading("Experience"),
];
for (const x of R.experience) {
  kids.push(rowLine([run(x.role, { bold: true }), run(`, ${x.org}, ${x.place}`)], x.dates));
  x.bullets.forEach((b) => kids.push(bullet(b)));
}
kids.push(heading("Projects"));
for (const p of R.projects) {
  kids.push(rowLine([run(p.name, { bold: true }), run(` | ${p.stack}`)], p.dates));
  p.bullets.forEach((b) => kids.push(bullet(b)));
}
kids.push(heading("Education"));
for (const x of R.education) {
  kids.push(rowLine([run(x.degree, { bold: true }), run(`, ${x.org}, ${x.place}`)], x.dates));
  if (x.note) kids.push(new Paragraph({ children: [run(x.note)], spacing: { after: 10 } }));
}

const doc = new Document({
  creator: R.name, title: `${R.name} Resume`,
  styles: { default: { document: { run: { font: BODY, size: SZ, color: INK } } } },
  numbering: {
    config: [{
      reference: "b",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 270, hanging: 180 } } } }],
    }],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 648, bottom: 576, left: 792, right: 792 } } },
    children: kids,
  }],
});
Packer.toBuffer(doc).then((buf) => {
  const out = path.join(ROOT, "resumes", "ats", "Agnel_Salve_Resume_ATS.docx");
  fs.writeFileSync(out, buf);
  console.log("wrote", out);
});
