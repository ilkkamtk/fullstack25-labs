document
  .querySelector("#login-form")
  .addEventListener("submit", async (event) => {
    event.preventDefault();

    const username = document.querySelector("#username").value;
    const password = document.querySelector("#password").value;

    //if(!username.length)
    if (username.trim().length === 0) {
      alert("Username is missing");
      return;
    }
    if (password.trim().length === 0) {
      alert("Password is missing");
      return;
    }

    const response = await fetch("/api/v1/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    console.log("data", data);

    console.log("credentials", { username, password });

    if (data.token) {
      window.localStorage.setItem("auth-token", data.token);

      // TODO: navigate user to some page
    }
  });
