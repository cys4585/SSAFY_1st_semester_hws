<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credential.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credential.password">
    </div>
    <button @click="login(credential)">로그인</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credential: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    ...mapActions(['login']),
  }
}
</script>
