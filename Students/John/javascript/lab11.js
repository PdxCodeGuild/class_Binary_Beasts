/*

all codes are written and created by John Robson Wed Mar 24, 2021

*/

const coins = {
  "half-dollars": 0.5,
  quarters: 0.25,
  dimes: 0.1,
  nickels: 0.05,
  pennies: 0.01,
};

export function runLab11() {
  renApp(
    [
      { el: "h1", text: "Lab 11 - Change Maker" },
      { el: "label", text: "How much money?" },
      { el: "span", cl: "change-span", text: "$" },
      { el: "input", cl: "change", min: 0, max: 10 },
      { el: "aside", cl: "coin-options" },
      { el: "div", cl: "change-return" },
    ],
    $("main")
  );

  renApp(
    [
      {
        el: "input",
        cl: "ckbox half-dollar",
        value: "half-dollars",
        type: "checkbox",
      },
      { el: "label", text: "No Half-Dollars" },
      { el: "input", cl: "ckbox quarter", value: "quarters", type: "checkbox" },
      { el: "label", text: "No Quarters" },
      { el: "input", cl: "ckbox dime", value: "dimes", type: "checkbox" },
      { el: "label", text: "No Dimes" },
      { el: "input", cl: "ckbox nickel", value: "nickels", type: "checkbox" },
      { el: "label", text: "No Nickles" },
      { el: "input", cl: "ckbox penny", value: "pennies", type: "checkbox" },
      { el: "label", text: "No Pennies" },
    ],
    $("aside")
  );

  $(".change").addEventListener("input", () => {
    checkInput($(".change"), 5);
  });
  $(".change").onchange = returnChange;
}

const returnChange = () => {
  checkValue($(".change"), 0, 100, false);
  let amount = $(".change").value,
    change = {};
  if (notNullV($(".change"))) {
    const checkboxes = $$(".ckbox");
    for (const [k, v] of Object.entries(coins)) {
      checkboxes.forEach((ckbox) => {
        if (!ckbox.checked) {
          if (ckbox.value === k) {
            change[k] = parseInt(
              Math.floor(Math.round(amount * 100) / 100 / v)
            );
            amount -= change[k] * v;
          }
        }
      });
    }
  }
  let elems = [];
  for (let [k, v] of Object.entries(change)) {
    if (v === 1) {
      if (k === "pennies") k = "penny";
      else k = k.slice(0, -1);
    }
    elems.push({ el: "p", cl: "change-returned", text: `${v} ${k}` });
  }
  clear($(".change-return"));
  renApp(elems, $(".change-return"));

  if (!$(".change-return").firstChild)
    renApp({ el: "p", text: "No Change" }, $(".change-return"));
};
