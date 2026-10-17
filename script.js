
async function runDemo() {
    const status = document.getElementById("status");
    const checks = document.getElementById("checks");
    const issues = document.getElementById("issues");
    const result = document.getElementById("result");

    status.textContent = "Connecting to security scanner...";
    result.textContent = "RUNNING";

    try {
        const response = await fetch("/api/results");

        if (!response.ok) {
            throw new Error("Could not load scan reports");
        }

        const data = await response.json();

        checks.textContent = data.checks;
        issues.textContent = data.issues;
        result.textContent = data.status;
        status.textContent = data.message;
    } catch (error) {
        result.textContent = "ERROR";
        status.textContent =
            "Scanner unavailable. Start the Flask application and run Jenkins first.";
    }
}
