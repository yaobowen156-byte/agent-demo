document.querySelectorAll("[data-copy]").forEach((button) => {
  button.addEventListener("click", async () => {
    const target = document.querySelector(button.dataset.copy);
    if (!target) return;

    const text = target.value ?? target.textContent ?? "";
    try {
      await navigator.clipboard.writeText(text.trim());
      const original = button.textContent;
      button.textContent = "已复制";
      setTimeout(() => {
        button.textContent = original;
      }, 1200);
    } catch {
      button.textContent = "复制失败";
      setTimeout(() => {
        button.textContent = "复制这段";
      }, 1200);
    }
  });
});

