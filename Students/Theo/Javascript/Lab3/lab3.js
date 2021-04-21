const h1 = document.querySelector("h1"),
  urls = [
    "www.google.com",
    "www.facebook.com",
    "www.amazon.com",
    "www.wikipedia.org",
  ];

setInterval(() => (h1.innerText = +h1.innerText - 1), 1000);

setTimeout(
  () => (window.location = `http://${urls[Math.floor(Math.random() * urls.length)]}`),
  5000
);
