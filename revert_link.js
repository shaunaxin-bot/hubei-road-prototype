const fs = require('fs');
const path = 'C:/AIprojects/roaddata/hubei/release/index.html';
let content = fs.readFileSync(path, 'utf8');

const searchString = '"\\u57FA\\u7840\\u7248")), /* @__PURE__ */ React.createElement("a", { href: "./project/20260808.html", target: "_blank", className: "text-slate-400 hover:text-blue-500 cursor-pointer ml-1 text-xs opacity-40 hover:opacity-100 transition-all", title: "\\u67E5\\u770B\\u6280\\u672F\\u8981\\u6C42" }, "\\u{1F517}"))), /* @__PURE__ */ React.createElement("div", { className: "flex items-center gap-3" }, !isStandalone && /* @__PURE__ */ React.createElement(';
const replacementString = '"\\u57FA\\u7840\\u7248")))), /* @__PURE__ */ React.createElement("div", { className: "flex items-center gap-3" }, !isStandalone && /* @__PURE__ */ React.createElement(';

if(content.includes(searchString)) {
    content = content.replace(searchString, replacementString);
    fs.writeFileSync(path, content, 'utf8');
    console.log("Success");
} else {
    console.log("Search string not found!");
}
