<template>
  <div id="app">
    <header class="header">
      <h1>🔮 사주 프로그램</h1>
      <p>생년월일과 시간을 입력하면 사주를 봐드립니다</p>
    </header>

    <main class="main">
      <!-- 입력 폼 -->
      <div class="form-container" v-if="!result">
        <h2>생년월일과 시간을 입력해주세요</h2>
        <form @submit.prevent="calculateSaju" class="saju-form">
          <div class="form-group">
            <label>생년월일</label>
            <div class="date-inputs">
              <input 
                v-model="formData.birth_year" 
                type="number" 
                placeholder="년도" 
                min="1900" 
                max="2100" 
                required
              >
              <input 
                v-model="formData.birth_month" 
                type="number" 
                placeholder="월" 
                min="1" 
                max="12" 
                required
              >
              <input 
                v-model="formData.birth_day" 
                type="number" 
                placeholder="일" 
                min="1" 
                max="31" 
                required
              >
            </div>
          </div>

          <div class="form-group">
            <label>생시</label>
            <div class="time-inputs">
              <input 
                v-model="formData.birth_hour" 
                type="number" 
                placeholder="시" 
                min="0" 
                max="23" 
                required
              >
              <input 
                v-model="formData.birth_minute" 
                type="number" 
                placeholder="분" 
                min="0" 
                max="59" 
                required
              >
            </div>
          </div>

          <div class="form-group">
            <label>성별</label>
            <select v-model="formData.gender" required>
              <option value="">선택해주세요</option>
              <option value="male">남성</option>
              <option value="female">여성</option>
            </select>
          </div>

          <button type="submit" :disabled="loading" class="submit-btn">
            {{ loading ? '계산 중...' : '사주 보기' }}
          </button>
        </form>
      </div>

      <!-- 결과 표시 -->
      <div class="result-container" v-if="result">
        <h2>🔮 사주 결과</h2>
        
        <div class="result-card">
          <h3>생년월일 정보</h3>
          <p><strong>생년월일:</strong> {{ result.birth_info.date }}</p>
          <p><strong>생시:</strong> {{ result.birth_info.time }}</p>
          <p><strong>성별:</strong> {{ result.birth_info.gender === 'male' ? '남성' : '여성' }}</p>
        </div>

        <div class="result-card">
          <h3>사주팔자</h3>
          <div class="saju-pillars">
            <div class="pillar">
              <span class="pillar-label">년주</span>
              <span class="pillar-value">{{ result.saju.year_pillar }}</span>
            </div>
            <div class="pillar">
              <span class="pillar-label">월주</span>
              <span class="pillar-value">{{ result.saju.month_pillar }}</span>
            </div>
            <div class="pillar">
              <span class="pillar-label">일주</span>
              <span class="pillar-value">{{ result.saju.day_pillar }}</span>
            </div>
            <div class="pillar">
              <span class="pillar-label">시주</span>
              <span class="pillar-value">{{ result.saju.hour_pillar }}</span>
            </div>
          </div>
        </div>

        <div class="result-card">
          <h3>오행 분석</h3>
          <div class="elements">
            <div class="element" v-for="(count, element) in result.elements" :key="element">
              <span class="element-name">{{ getElementName(element) }}</span>
              <span class="element-count">{{ count }}</span>
            </div>
          </div>
        </div>

        <div class="result-card">
          <h3>운세 해석</h3>
          <p class="fortune-text">{{ result.fortune }}</p>
        </div>

        <div class="result-card ai-interpretation" v-if="result.ai_interpretation">
          <h3>🤖 AI 상세 해석</h3>
          <div class="ai-content">
            <p class="ai-text">{{ result.ai_interpretation }}</p>
          </div>
        </div>

        <button @click="resetForm" class="reset-btn">다시 계산하기</button>
      </div>

      <!-- 에러 메시지 -->
      <div class="error-message" v-if="error">
        <p>{{ error }}</p>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      formData: {
        birth_year: '',
        birth_month: '',
        birth_day: '',
        birth_hour: '',
        birth_minute: '',
        gender: ''
      },
      result: null,
      loading: false,
      error: null,
      // 개발 환경에서는 로컬 서버, 배포 시에는 실제 API URL로 변경
      apiUrl: 'https://saju-backend-vu8s.onrender.com'
    }
  },
  methods: {
    async calculateSaju() {
      this.loading = true
      this.error = null
      
      try {
        const response = await axios.post(`${this.apiUrl}/api/saju`, this.formData)
        this.result = response.data.data
      } catch (error) {
        console.error('API 호출 오류:', error)
        this.error = '사주 계산 중 오류가 발생했습니다. 다시 시도해주세요.'
      } finally {
        this.loading = false
      }
    },
    resetForm() {
      this.formData = {
        birth_year: '',
        birth_month: '',
        birth_day: '',
        birth_hour: '',
        birth_minute: '',
        gender: ''
      }
      this.result = null
      this.error = null
    },
    getElementName(element) {
      const elementNames = {
        wood: '목(木)',
        fire: '화(火)',
        earth: '토(土)',
        metal: '금(金)',
        water: '수(水)'
      }
      return elementNames[element] || element
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  color: #333;
}

#app {
  min-height: 100vh;
  padding: 20px;
}

.header {
  text-align: center;
  color: white;
  margin-bottom: 40px;
}

.header h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.header p {
  font-size: 1.1rem;
  opacity: 0.9;
}

.main {
  max-width: 800px;
  margin: 0 auto;
}

.form-container, .result-container {
  background: white;
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.form-container h2, .result-container h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.saju-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 600;
  color: #555;
}

.date-inputs, .time-inputs {
  display: flex;
  gap: 10px;
}

.date-inputs input, .time-inputs input {
  flex: 1;
  padding: 12px;
  border: 2px solid #e1e5e9;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.date-inputs input:focus, .time-inputs input:focus {
  outline: none;
  border-color: #667eea;
}

select {
  padding: 12px;
  border: 2px solid #e1e5e9;
  border-radius: 8px;
  font-size: 16px;
  background: white;
  cursor: pointer;
}

.submit-btn, .reset-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 15px 30px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s;
}

.submit-btn:hover, .reset-btn:hover {
  transform: translateY(-2px);
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.result-card {
  background: #f8f9fa;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
  border-left: 4px solid #667eea;
}

.result-card h3 {
  color: #333;
  margin-bottom: 15px;
}

.saju-pillars {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 15px;
}

.pillar {
  text-align: center;
  padding: 15px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.pillar-label {
  display: block;
  font-size: 12px;
  color: #666;
  margin-bottom: 5px;
}

.pillar-value {
  display: block;
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.elements {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 10px;
}

.element {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: white;
  border-radius: 6px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.element-name {
  font-weight: 600;
}

.element-count {
  background: #667eea;
  color: white;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: bold;
}

.fortune-text {
  font-size: 16px;
  line-height: 1.6;
  color: #555;
  background: white;
  padding: 15px;
  border-radius: 8px;
  border-left: 4px solid #28a745;
}

.error-message {
  background: #f8d7da;
  color: #721c24;
  padding: 15px;
  border-radius: 8px;
  border: 1px solid #f5c6cb;
  margin-top: 20px;
  text-align: center;
}

.reset-btn {
  width: 100%;
  margin-top: 20px;
}

.ai-interpretation {
  border-left: 4px solid #10b981;
  background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
}

.ai-content {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.ai-text {
  font-size: 16px;
  line-height: 1.8;
  color: #374151;
  white-space: pre-line;
}

@media (max-width: 600px) {
  .header h1 {
    font-size: 2rem;
  }
  
  .date-inputs, .time-inputs {
    flex-direction: column;
  }
  
  .saju-pillars {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style> 