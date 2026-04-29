document.querySelectorAll("[data-copy]").forEach((button) => {
  button.addEventListener("click", async () => {
    const target = document.querySelector(button.dataset.copy);
    if (!target) return;

    const text = target.value ?? target.textContent ?? "";
    const original = button.textContent;

    try {
      await navigator.clipboard.writeText(text.trim());
      button.textContent = "已复制";
    } catch {
      button.textContent = "复制失败";
    }

    setTimeout(() => {
      button.textContent = original;
    }, 1200);
  });
});
