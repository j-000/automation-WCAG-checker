import axios from 'axios';

const ApiClient = axios.create({
  baseURL: 'http://localhost:5000/api/v1',
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type':'application/json'
  }
})

export default {
  verify(token){
    return ApiClient.get('/authenticate', {
      headers:{
      'Authorization': `Bearer ${token}`
      }
    })
  },
  registerUser(payload){
    return ApiClient.post('/register', payload)
  },
  authenticate(email, password){
    return ApiClient.post('/authenticate', {
      email,
      password
    })
  }
  
}
