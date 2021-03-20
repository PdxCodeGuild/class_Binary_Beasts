/*

all codes are written and created by John Robson Fri Mar 19, 2021

*/

const eyes = [":", ";", "8", ">:", ":'", "X"];
const noses = ["", "-", "^"];
const mouths = [")", "(", "*", "$", "O", "P", "D", "C", "3", "/"];

const armsV = ["", "<>", "\\/"];
const cheeksV = ["", "()", "[]", "{}"];
const eyesV = ["-", "^", "o", "@", "v", "O", "u"];
const mouthsV = ["_", ".", "o"];

export function runLab05() {
  renApp(
    [
      { el: "h1", text: "Lab 05 - Emoticon Generator" },
      { el: "button", text: "Generate Emoticon", cl: "emoticon-btn" },
    ],
    $("main")
  );

  $(".emoticon-btn").onclick = generateEmoticon;
}

const generateEmoticon = () => {
  limit($$(".emo"), 5)
  const emoteH = rand(eyes) + rand(noses) + rand(mouths),
    aV = rand(armsV),
    cV = rand(cheeksV),
    eV = rand(eyesV),
    mV = rand(mouthsV);
  let emoteV = aV === "" ? "" : aV[0];
  emoteV += cV === "" ? "" : cV[0];
  emoteV += eV + mV + eV;
  emoteV += cV === "" ? "" : cV[1];
  emoteV += aV === "" ? "" : aV[1];
  renApp({ el: "p", cl: "emo", text: rand([emoteH, emoteV]) }, $("main"));
};
