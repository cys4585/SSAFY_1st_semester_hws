<template>
  <div id="app">
    <h1>App.vue</h1>
    <TodoForm/>
    <TodoList/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from "@/components/TodoList"

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
  border: solid 4px;
  padding: 1rem;
}
</style>
