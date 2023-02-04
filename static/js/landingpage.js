let name;
const BASE_URL = "localhost:5000";

const init = () => {
  console.log(window.location);
};

const handleKeyUpUserName = () => {
  if (event.key !== "Enter") return;
  handleClickStartBtn();
};

const handleClickStartBtn = () => {
  const nickname = document.getElementById("nickname").value;
  name = nickname;
  postName(nickname);
};

const postName = (name_give) => {
  fetch(`http://${BASE_URL}/api/nickname`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      name_give,
    }),
  })
    .then((res) => res.json())
    .then((data) => alert(data.msg))
    .then((v) => (window.location.href = "/mainpage"));
};