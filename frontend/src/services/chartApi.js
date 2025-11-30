export async function fetchChartKeysRequest(timeframe, token) {
    const res = await fetch(`http://localhost:8000/charts/${timeframe}/keys`, {
        headers: { Authorization: `Bearer ${token}`}
    })

    if (!res.ok) {
        throw new Error(`Failed to fetch chart (${res.status})`)
    }

    const data = await res.json()
    if (!data.keys || !data.keys.length) {
        throw new Error("No chart keys found")
    }

    return data.keys
}

export async function fetchChartByKeyRequest(key, token) {
    const res = await fetch(`http://localhost:8000/charts/key/${key}`, {
        headers: { Authorization: `Bearer ${token}`}
    })

    if (!res.ok) {
        throw new Error(`Failed to fetch chart for date: ${key}(${res.status})`)
    }

    const data = await res.json()
    return data.chart_data
}