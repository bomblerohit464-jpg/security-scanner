
function runDemo() {
    const status = document.getElementById("status");
    status.textContent = "Running demo security scan...";

    document.getElementById("checks").textContent = "4";
    document.getElementById("issues").textContent = "0";
    document.getElementById("result").textContent = "DEMO";

    status.textContent =
        "Demo complete. These are simulated results, not a real scan.";
}
