console.log("api.js loaded");

const API_BASE_URL = "http://localhost:8000/api";

async function getAnimals() {
    const res = await fetch(`${API_BASE_URL}/animals`);
    return await res.json();
}

async function getAnimal(id) {
    const res = await fetch(`${API_BASE_URL}/animals/${id}`);
    return await res.json();
}

async function putAnimal(id, animal) {
    const res = await fetch(`${API_BASE_URL}/animals/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(animal)
    });

    if (!res.ok) {
        const error = await res.json();
        throw new Error(error.detail || "Failed to update animal (PUT)");
    }

    return await res.json();
}


async function patchAnimal(id, data) {
    const res = await fetch(`${API_BASE_URL}/animals/${id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    if (!res.ok) {
        const error = await res.json();
        throw new Error(error.detail || "Failed to update animal (PATCH)");
    }

    return await res.json();
}


async function deleteAnimal(id) {
    const res = await fetch(`${API_BASE_URL}/animals/${id}`, {
        method: "DELETE"
    });

    if (!res.ok) {
        const error = await res.json();
        throw new Error(error.message || "Failed to delete");
    }

    return await res.json();
}

async function createAnimal(data) {
    const res = await fetch(`${API_BASE_URL}/animals`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    if (!res.ok) {
        const error = await res.json();
        throw new Error(error.message || "Failed to create");
    }

    return await res.json();
}

