// script.js

document.getElementById("logo").addEventListener("click", function () {
  // Oculta a tela de introdução e exibe o formulário de login com animação
  document.querySelector(".intro-container").style.opacity = 0;
  document.getElementById("loginContainer").classList.add("show-login");

  // Remove a tela de introdução após a transição
  setTimeout(() => {
      document.querySelector(".intro-container").style.display = "none";
  }, 500); // Tempo em milissegundos correspondente à transição
});

// Validação simples de login para demonstrar a transição
document.getElementById("loginForm").addEventListener("submit", function (event) {
  event.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Exemplo de autenticação simples
  if (username === "admin" && password === "1234") {
      document.getElementById("message").textContent = "Login bem-sucedido!";
      document.getElementById("message").style.color = "#00FF00";
  } else {
      document.getElementById("message").textContent = "Usuário ou senha incorretos.";
  }
});
