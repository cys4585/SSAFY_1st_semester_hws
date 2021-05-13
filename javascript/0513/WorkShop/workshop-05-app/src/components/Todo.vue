<template>
  <div id="todo">
    <span @click="updateTodo(todo)" :class="{ completed: todo.completed }">
      {{ todo.title }}
    </span>
    <button @click="deleteTodo(todo)">삭제</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Todo',
  props: {
    todo: {
      type: Object,
    }
  },
  methods: {
    ...mapActions(['deleteTodo', 'updateTodo'])
  }
}
</script>

<style>
  #todo {
    border: 4px solid yellowgreen;
    margin: 0.4rem 20rem;
  }
  .completed {
    text-decoration: line-through;
  }
</style>