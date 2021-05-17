<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in todos" :key="idx">
        <span @click="updateTodoStatus(todo)" :class="{ completed: todo.completed }">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoList',
  data: function () {
    return {}
  },
  methods: {
    ...mapActions(['deleteTodo', 'updateTodoStatus']),
    },
  created: function () {
    this.$store.dispatch('getTodosFromServer')
  },
  computed: {
    todos: function () {
      return this.$store.state.todos
    }
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
