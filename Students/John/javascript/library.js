/*

This Library was written and created by John Robson Thu Mar 18, 2021

*/

const lowers = "abcdefghijklmnopqrstuvwxyz";
const uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const specials = "!@#$%^&*()_+-=[]{};':\",./<>?\\|`~";
const numbers = "0123456789";

const app = (els, el) => arr(els).forEach((e) => el.append(e));

const renApp = (els, el) => arr(els).forEach((e) => el.append(ren(e)));

const arr = (arr) => (!Array.isArray(arr) ? [arr] : arr);

const rand = (arr) => arr[Math.floor(Math.random() * arr.length)];

const randI = (arr, t) => {
  let arr2 = [];
  for (let i = 0; i < t; i++) {
    arr2.push(rand(arr));
  }

  return arr2;
};

const randN = (min, max) => Math.floor(Math.random() * max + min);

const ren = ({ el, cl, text, type, html, value, min, max }) => {
  const elem = document.createElement(el);
  if (cl != null) elem.className = cl;
  if (text != null) elem.innerText = text;
  if (type != null) elem.type = type;
  if (html != null) elem.innerHTML = html;
  if (value != null) elem.value = value;
  if (min != null) elem.min = min;
  if (max != null) elem.max = max;
  return elem;
};

const $ = (el) => document.querySelector(el);

const $$ = (el) => document.querySelectorAll(el);

const clear = (el) => {
  while (el.firstChild) el.firstChild.remove();
};

const notNull = (args) => {
  let check = true;

  arr(args).forEach((a) => {
    if (a == null || a === "") check = false;
  });

  return check;
};

const notNullV = (args) => {
  let check = true;

  arr(args).forEach((a) => {
    if (a.value == null || a.value === "") check = false;
  });

  return check;
};

const shuffle = (arr) => {
  var i = arr.length,
    t,
    rI;

  while (0 !== i) {
    rI = Math.floor(Math.random() * i);
    i--;
    t = arr[i];
    arr[i] = arr[rI];
    arr[rI] = t;
  }

  return arr;
};

const checkInput = (el, i) => {
  if (!parseInt(el.value)) el.value = null;
  if (i != null) if (el.value.length > i) el.value = el.value.substring(1);
};

const checkValue = (el, min, max) => {
  if (el.value < min) el.value = min;
  else if (el.value > max) el.value = max;
  else el.value = Math.round(el.value);
};

const equals = (a, b) => a.length === b.length && a.every((v, i) => v === b[i]);

const limit = (els, i) => (els.length > i - 1 ? els[0].remove() : "");

const within = (el, arr) => {
  if (typeof arr === "string") arr = arr.split("");
  check = "false";
  arr.forEach((a) => {
    if (a === el) check = "true";
  });

  if (el === " ") return el;

  return check === "true" ? el : "";
};

const build = (value, count, d = "", bar, fill) => {
  let buf = "";
  j = 0;
  for (let i = 0; i < count; i++) {
    buf += value + d;
    j++;
  }
  for (j; j < bar; j++) buf += fill + d;
  return buf;
};
