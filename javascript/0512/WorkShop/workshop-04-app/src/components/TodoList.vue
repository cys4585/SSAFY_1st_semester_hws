<template>
  <div id="todo-list">
    <h1>TodoList.vue</h1>
    <ul>
      <Todo/>
      <Todo/>
      <Todo/>
    </ul>
  </div>
</template>

<script>
import Todo from '@/components/Todo'

export default {  
  name: 'TodoList',
  components: {
    Todo
  }
}
</script>

<style>
  #todo-list {
    border: solid 4px green;
    margin: 0 10rem;
    padding: 0 0 2rem 0;
  }
</style>