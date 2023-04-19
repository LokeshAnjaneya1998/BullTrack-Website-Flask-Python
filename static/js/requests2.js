async function post(url, data) {
    const response = fetch(url, { method: "POST", headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
    return (await response).json();
}