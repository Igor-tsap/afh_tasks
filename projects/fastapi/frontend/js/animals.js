console.log("animals.js loaded");


document.addEventListener("DOMContentLoaded", init);

async function init() {
    setupCreateForm();

    try {
        const animals = await getAnimals();
        renderAnimals(animals);
    } catch (err) {
        showError(err.message);
    }
}

document.getElementById("animals-list").addEventListener("click", async (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;

    const card = btn.closest(".animal-card");
    const id = card.dataset.id;

    if (btn.dataset.action === "edit") {
        window.location.href = `animals.html?id=${id}`;
    }

    if (btn.dataset.action === "delete") {
        if (!confirm("Delete this animal?")) return;

        try {
            await deleteAnimal(id);
            card.remove();
        } catch (err) {
            alert(err.message);
        }
    }
});


function renderAnimals(animals) {
    const container = document.getElementById("animals-list");
    container.innerHTML = "";

    animals.forEach(animal => {
        const card = document.createElement("div");
        card.className = "animal-card";
        card.dataset.id = animal.id;

        const imgSrc = animal.img && animal.img.trim() !== "" ? animal.img : "/images/placeholder.jpg";

        card.innerHTML = `
            <h3>${animal.name}</h3>
            <img src="${imgSrc}" alt="${animal.name}">
            <p>Price: ${animal.price}</p>
            <p>Quantity: ${animal.quantity}</p>
            <div class="animal-buttons">
                <button class="edit-btn" data-action="edit">Edit</button>
                <button class="delete-btn" data-action="delete">Delete</button>
            </div>
        `;

        container.appendChild(card);
    });
}




function showError(message) {
    const container = document.getElementById("animals-list");
    container.innerHTML = `<p class="error">Error: ${message}</p>`;
}



function setupCreateForm() {
    const form = document.getElementById("create-animal-form");
    const status = document.getElementById("create-status");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = {
            name: formData.get("name"),
            price: Number(formData.get("price")),
            quantity: Number(formData.get("quantity")),
            img: formData.get("img")
        };

        try {
            await createAnimal(data);

            const animals = await getAnimals();
            renderAnimals(animals);

            status.textContent = "Animal added";
            status.style.color = "green";
            form.reset();
        } catch (err) {
            status.textContent = err.message;
            status.style.color = "red";
        }
    });
}

