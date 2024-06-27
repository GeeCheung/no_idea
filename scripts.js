document.addEventListener("DOMContentLoaded", function () {
  const API_URL = "https://4bj0f1g0-5001.uks1.devtunnels.ms/posts"; // Update this if your API is hosted elsewhere

  function fetchPosts() {
    fetch(API_URL)
      .then((response) => response.json())
      .then((posts) => {
        const postsList = document.getElementById("posts");
        postsList.innerHTML = "";
        posts.forEach((post) => {
          const li = document.createElement("li");
          li.textContent = `${post.title}: ${post.body}`;
          postsList.appendChild(li);
        });
      })
      .catch((error) => console.error("Error fetching posts:", error));
  }

  document
    .getElementById("postForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      const title = document.getElementById("title").value;
      const body = document.getElementById("body").value;

      fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, body, userId: 1 }),
      })
        .then((response) => response.json())
        .then((post) => {
          console.log("Post created:", post);
          fetchPosts();
        })
        .catch((error) => console.error("Error creating post:", error));
    });

  // Fetch posts on page load
  fetchPosts();
});
