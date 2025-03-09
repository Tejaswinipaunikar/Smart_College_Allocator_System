document.addEventListener("DOMContentLoaded", function () {
    console.log("Script loaded");

    const form = document.getElementById("college-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form refresh

        const percentile = document.getElementById("percentile").value;
        const exam = document.getElementById("exam").value;

        if (!percentile || percentile < 0 || percentile > 100) {
            alert("Please enter a valid percentile (0-100).");
            return;
        }

        fetch("/get_colleges", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ percentile, exam }),
        })
        .then(response => response.json())
        .then(data => {
            console.log("Received data:", data);
            const resultDiv = document.getElementById("result");
            resultDiv.innerHTML = "";

            if (!Array.isArray(data) || data.length === 0) {
                resultDiv.innerHTML = "<p style='color:darkred; font-weight:bold;'>No colleges found for your percentile.</p>";
                return;
            }

            let output = "<h3>Eligible Colleges:</h3><ul style='list-style-type: none; padding-left: 0;'>";

            data.forEach((college, index) => {
                output += `
                    <li>
                        <h2 style="font-weight:bold; font-size:1.5em;">
                            ${index + 1}. ${college.name} 
                        </h2>
                        <p><strong>${college.description || "No description available"}</strong></p>
                        <ul>
                            <li><strong>Branches:</strong></li>
                            <ul style="margin-left: 20px;">
                                ${Array.isArray(college.branches) && college.branches.length > 0
                                    ? college.branches.map(branch => `<li>${branch}</li>`).join("")
                                    : "<li>Branch data unavailable</li>"
                                }
                            </ul>
                            <li><strong>Annual Fees:</strong> ₹${college.fees || "Not Available"}</li>
                            <li><strong>Website:</strong> <a href="${college.website}" target="_blank" 
                                style="color: yellow; font-weight: bold; text-decoration: none;">${college.website}</a></li>
                        </ul>
                    </li>
                `;
            });

            output += "</ul>";
            resultDiv.innerHTML = output;

            // **Force scroll to the top after inserting data**
            setTimeout(() => {
                window.scrollTo({ top: 0, behavior: "smooth" });
            }, 100);
        })
        .catch(error => {
            console.error("Error fetching colleges:", error);
            resultDiv.innerHTML = "<p style='color:red; font-weight:bold;'>An error occurred while fetching colleges.</p>";
        });
    });
});
