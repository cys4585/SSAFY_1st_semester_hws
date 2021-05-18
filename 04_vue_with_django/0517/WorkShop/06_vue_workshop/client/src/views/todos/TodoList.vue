<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in todos" :key="idx">
        <span @click="updateTodoStatus({todo, token})" :class="{ completed: todo.completed }">{{ todo.title }}</span>
        <button @click="deleteTodo({todo, token})" class="todo-btn">X</button>
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
  computed: {
    token: function () {
      return this.$store.state.token
    },
    todos: function () {
      return this.$store.state.todos
    }
  },
  methods: {
    ...mapActions(['getTodos', 'deleteTodo', 'updateTodoStatus']),
  },
  created: function () {
    this.getTodos(this.token)
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
