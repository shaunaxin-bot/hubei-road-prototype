const fs = require('fs');
const filePath = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html';
let content = fs.readFileSync(filePath, 'utf8');

content = content.replace(
    '<td rowspan="5" class="p-2.5 font-bold text-brand-800 bg-blue-50/40 border-r border-slate-200 align-top">初步验收</td>',
    '<td rowspan="10" class="p-2.5 font-bold text-brand-800 bg-blue-50/40 border-r border-slate-200 align-top">初步验收</td>'
);

content = content.replace(
    /[ \t]*<td rowspan="2" class="p-2.5 font-bold text-brand-800 bg-blue-50\/40 border-r border-slate-200 align-top">平台演示<\/td>\r?\n/g,
    ''
);

content = content.replace(
    /[ \t]*<td rowspan="3" class="p-2.5 font-bold text-brand-800 bg-blue-50\/40 border-r border-slate-200 align-top">过程成果<\/td>\r?\n/g,
    ''
);

fs.writeFileSync(filePath, content, 'utf8');
console.log("Success");
