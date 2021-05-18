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
  computed: {
    config: function () {
      return this.$store.getters.config
    }
  },
  methods: {
    createTodo: function () {
      this.$store.dispatch('createTodo', this.title, this.config)
      this.title = ''
    }
  },
}
</script>
