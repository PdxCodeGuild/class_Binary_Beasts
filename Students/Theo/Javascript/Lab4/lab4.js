const url = "https://favqs.com/api/qotd"

const addToPage = (x, y) => {
	h = document.createElement("h3")
	p = document.createElement("p");
	h.innerText = (x);
	p.innerText = (`-${y}`);
	document.body.append(h)
	document.body.append(p);
}

fetch(url)
  .then((response) => response.json())
  .then((json) => addToPage(json.quote.body, json.quote.author));