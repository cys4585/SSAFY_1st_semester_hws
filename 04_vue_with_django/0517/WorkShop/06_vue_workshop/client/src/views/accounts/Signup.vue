<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model=credential.username>
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model=credential.password>
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model=credential.passwordConfirmation>
    </div>
    <button @click="signup(credential)">회원가입</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credential: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>
