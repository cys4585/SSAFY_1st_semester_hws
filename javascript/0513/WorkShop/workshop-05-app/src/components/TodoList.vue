<template>
  <div id="todo-list">
    <h1>TodoList</h1>
    <ul>
      <Todo
        v-for="(todo, idx) in getTodoList"
        :key="idx"
        :todo="todo"
      />
    </ul>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Todo from '@/components/Todo'

export default {  
  name: 'TodoList',
  components: {
    Todo
  },
  computed: {
    ...mapGetters(['getTodoList',])
  },
}
</script>

<style>
  #todo-list {
    border: solid 4px green;
    margin: 0 10rem;
    padding: 0 0 2rem 0;
  }
</style>