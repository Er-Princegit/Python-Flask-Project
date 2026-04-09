function nextStep(step) {
    let current = document.getElementById("step" + step);
    let next = document.getElementById("step" + (step + 1));

    let select = current.querySelector("select");
    if (select && select.value === "") {
        alert("Please select an option!");
        return;
    }

    current.classList.remove("active");
    next.classList.add("active");

    // 🔥 when moving from semester → subject
    if (step === 2) {
        updateSubjects();
    }
}

// 🔥 ADVANCED SUBJECT LOGIC
function updateSubjects() {
    let branch = document.querySelector("select[name='branch']").value;
    let semester = document.querySelector("select[name='semester']").value;
    let subjectDropdown = document.querySelector("select[name='subject']");

    subjectDropdown.innerHTML = "";

    let data = {
        "CSE": {
            "1": ["Maths", "Physics", "Basic Programming"],
            "2": ["Data Structures", "Digital Logic"],
            "3": ["OOP", "DBMS", "OS"],
            "4": ["Computer Networks", "AI"]
        },
        "ECE": {
            "1": ["Maths", "Physics"],
            "2": ["Circuits", "Signals"],
            "3": ["Microprocessors", "Communication"],
            "4": ["VLSI", "Embedded Systems"]
        },
        "ME": {
            "1": ["Maths", "Physics"],
            "2": ["Mechanics", "Thermodynamics"],
            "3": ["Fluid Mechanics", "Machine Design"],
            "4": ["Heat Transfer", "Production"]
        },
        "CE": {
            "1": ["Maths", "Physics"],
            "2": ["Engineering Mechanics"],
            "3": ["Structures", "Geotechnical"],
            "4": ["Transportation", "Survey"]
        }
    };

    if (data[branch] && data[branch][semester]) {
        data[branch][semester].forEach(sub => {
            let option = document.createElement("option");
            option.value = sub;
            option.text = sub;
            subjectDropdown.appendChild(option);
        });
    }
}