/*

This Library was written and created by John Robson Thu Mar 18, 2021

*/

function app(els, el) {
  arr(els).forEach((e) => el.append(e));
}

function renApp(els, el) {
  arr(els).forEach((e) => el.append(ren(e)));
}

function arr(arr) {
  return !Array.isArray(arr) ? [arr] : arr
}

function rand(list) {
  let i = Math.round(Math.random() * (list.length - 1));
  return list[i];
}

function ren({ el, cl, text, type, html, value, min, max }) {
  const elem = document.createElement(el);
  if (cl != null) elem.className = cl;
  if (text != null) elem.innerText = text;
  if (type != null) elem.type = type;
  if (html != null) elem.innerHTML = html;
  if (value != null) elem.value = value;
  if (min != null) elem.min = min;
  if (max != null) elem.max = max;
  return elem;
}

function $(el, p) {
  if (!p) return document.querySelector(el);
  else return p.querySelector(el);
}

function $$(el) {
  return document.querySelectorAll(el);
}

function clear(el) {
  while (el.firstChild) el.firstChild.remove();
}