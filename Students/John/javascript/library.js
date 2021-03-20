/*

This Library was written and created by John Robson Thu Mar 18, 2021

*/

const lowers = "abcdefghijklmnopqrstuvwxyz";
const uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const special = "!@#$%^&*()_+-=[]{};':\",./<>?\\|`~";
const numbers = "0123456789";

const app = (els, el) => {
  arr(els).forEach((e) => el.append(e));
};

const renApp = (els, el) => {
  arr(els).forEach((e) => el.append(ren(e)));
};

const arr = (arr) => !Array.isArray(arr) ? [arr] : arr;

const rand = (list) => list[Math.round(Math.random() * (list.length - 1))];

const randI = (list, t) => {
  let arr = [];
  for (let i = 0; i < t; i++) {
    arr.push(rand(list));
  }

  return arr;
};

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

const limit = (els, i) => arr(els).length > i - 1 ? arr(els)[0].remove() : "";