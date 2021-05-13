<template>
  <div id="todo-form">
    <input type="text" 
      @keyup.enter="addTodo(todoTitle)"
      v-model.trim="todoTitle"
    >
    <button @click="addTodo(todoTitle)">add</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoForm',
  methods: {
    ...mapActions(['addTodo',])
  },
  data: function () {
    return {
      todoTitle: '',
    }
  },
}
</script>

<style scoped>
  #todo-form {
    border: solid 4px skyblue;
    margin: 2rem 20rem;
    padding: 1rem;
  }
</style>