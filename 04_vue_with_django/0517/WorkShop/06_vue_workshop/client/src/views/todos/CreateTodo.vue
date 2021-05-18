<template>
  <div>
    <input type="text" v-model.trim="title" @keyup.enter="createTodo">
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: '',
    }
  },
  computed: {
    token: function () {
      return this.$store.state.token
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.title,
      }
      if (todoItem.title && this.token) {
        const config = { Authorization: `JWT ${this.token}` }
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/todos/',
          data: todoItem,
          headers: config
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'TodoList' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  }
}
</script>
