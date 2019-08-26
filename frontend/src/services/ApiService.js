import axios from 'axios';

const ApiClient = axios.create({
  baseURL: 'http://localhost:5000/api/v1',
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type':'application/json'
  }
})

var auth_header = (token) =>  { return {headers:{'Authorization': `Bearer ${token}`}}}

export default {
  register_user(payload){
    return ApiClient.post('/register', payload)
  },
  delete_account(token){
    return ApiClient.delete('/register', auth_header(token))    
  },
  authenticate(email, password){
    return ApiClient.post('/authenticate', {email, password})
  },
  logout(token){
    return ApiClient.delete('/authenticate', auth_header(token))
  },
  update_user(token){
    return ApiClient.get('/authenticate', auth_header(token))
  },
  get_user_reports(userid, token){
    return ApiClient.get(`/user/${userid}/reports`, auth_header(token))
  },
  get_report_by_hid(token, userid, reporthid){
    return ApiClient.get(`/user/${userid}/reports/${reporthid}`, auth_header(token))
  },
  start_scan(token, payload){
    return ApiClient.post('/scans', payload, auth_header(token))
  }
}
