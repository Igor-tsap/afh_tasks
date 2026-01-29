// frontend/static/js/animals.js

document.addEventListener("DOMContentLoaded", async () => {
    try {
        const animals = await getAnimals();
        renderAnimals(animals);
    } catch (err) {
        showError(err.message);
    }
});

function renderAnimals(animals) {
    const container = document.getElementById("animals-list");
    container.innerHTML = "";

    if (!animals.length) {
        container.textContent = "No animals found.";
        return;
    }

    animals.forEach(animal => {
        const card = document.createElement("div");
        card.className = "animal-card";

        card.innerHTML = `
            <h3>${animal.name}</h3>
            ${animal.img ? `<img src="${animal.img}" alt="${animal.name}">` : ""}
            <p>Price: ${animal.price}</p>
            <p>Quantity: ${animal.quantity}</p>
            <div class="animal-buttons">
                <button class="edit-btn">Edit</button>
                <button class="delete-btn">Delete</button>
            </div>
        `;

        // Delete button
        card.querySelector(".delete-btn").addEventListener("click", async () => {
            if (confirm(`Are you sure you want to delete ${animal.name}?`)) {
                try {
                    await deleteAnimal(animal.id);
                    card.remove(); // remove from DOM immediately
                } catch (err) {
                    alert("Error deleting: " + err.message);
                }
            }
        });

        // Edit button
        card.querySelector(".edit-btn").addEventListener("click", () => {
            // Go to animal detail page with id in query
            window.location.href = `animals.html?id=${animal.id}`;
        });

        container.appendChild(card);
    });
}

function showError(message) {
    const container = document.getElementById("animals-list");
    container.innerHTML = `<p class="error">Error: ${message}</p>`;
}

document.addEventListener("DOMContentLoaded", () => {
    setupCreateForm();
});

function setupCreateForm() {
    const form = document.getElementById("create-animal-form");
    const status = document.getElementById("create-status");
    const container = document.getElementById("animals-list");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = {
            name: formData.get("name"),
            price: parseFloat(formData.get("price")),
            quantity: parseInt(formData.get("quantity")),
            img: formData.get("img")
        };

        try {
            const result = await createAnimal(data);

            // Add the new animal to the list without reload
            const animals = await getAnimals();
            renderAnimals(animals);

            status.textContent = "Animal added successfully!";
            status.style.color = "green";
            form.reset();
        } catch (err) {
            status.textContent = "Error: " + err.message;
            status.style.color = "red";
        }
    });
}
