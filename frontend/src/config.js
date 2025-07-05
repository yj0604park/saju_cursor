// 환경별 설정
const config = {
  development: {
    apiUrl: 'http://localhost:8000'
  },
  production: {
    apiUrl: 'https://saju-backend-vu8s.onrender.com'
  }
}

// 현재 환경 감지
const isDevelopment = import.meta.env.DEV
const currentConfig = isDevelopment ? config.development : config.production

// 환경 변수가 있으면 우선 사용
if (import.meta.env.VITE_API_URL) {
  currentConfig.apiUrl = import.meta.env.VITE_API_URL
}

export default currentConfig 