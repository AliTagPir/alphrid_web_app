export async function loginRequest(username, password) {
  const res = await fetch('http://localhost:8000/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  })

  if (!res.ok) {
    const err = await res.json()
    throw new Error(err.detail || 'Login failed')
  }

  return await res.json()
}

export async function fetchUserInfoRequest(token) {
  const res = await fetch('http://localhost:8000/auth/me', {
    method: 'GET',
    headers: { Authorization: `Bearer ${token}` }
  })

  if (!res.ok) {
    const err = await res.json()
    throw new Error(err.detail || 'Failed to fetch user info')
  }

  return await res.json()
}