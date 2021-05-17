<template>
  <div>
    <input type="text" v-model.trim="title" @keyup.enter="createTodo">
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: '',
    }
  },
  methods: {
    createTodo: function () {
      this.$store.dispatch('createTodo', this.title)
      this.title = ''
    }
  }
}
</script>
