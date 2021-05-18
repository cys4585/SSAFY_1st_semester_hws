import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: null,
    isLogin: false,
    todos: [],
  },
  mutations: {
    CHECK_LOGIN: function (state) {
      const token = localStorage.getItem('jwt')
      if (token) {
        state.token = token
        state.isLogin = true
      } else {
        state.token = null
        state.isLogin = false
      }
    },
    SET_TODOS: function (state, todos) {
      state.todos = todos
    },
    DELETE_TODO: function (state, deletedTodo) {
      // todos의 원소 중에서, deletedTodo 삭제
      // 나머지로 todos 갱신
      state.todos = state.todos.filter(todo => {
        return todo !== deletedTodo
      })
    },
    UPDATE_TODO_STATUS: function (state, updatedTodo) {
      state.todos = state.todos.map(todo => {
        if (todo.id === updatedTodo.id) {
          todo.completed = updatedTodo.completed
        }
        return todo
      })
    }
  },
  actions: {
    signup: function (context, credential) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: credential,
      })
        .then(function () {
          router.push({ name: 'Login' })
        })
    },
    login: function (context, credential) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: credential,
      })
        .then(res => {
          const token = res.data.token
          localStorage.setItem('jwt', token)
          context.commit('CHECK_LOGIN')
          router.push({ name: 'TodoList' })
        })
    },
    logout: function (context) {
      localStorage.removeItem('jwt')
      context.commit('CHECK_LOGIN')
      router.push({ name: 'Login' })
    },
    checkLogin: function (context) {
      context.commit('CHECK_LOGIN')
    },
    getTodos: function ({ commit }, token) {
      if (token) {
        const config = { Authorization: `JWT ${token}` }
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/todos/',
          headers: config,
        })
          .then((res) => {
            const todos = res.data
            commit('SET_TODOS', todos)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    deleteTodo: function ({ commit }, { todo, token }) {
      if (token) {
        const config = { Authorization: `JWT ${token}` }
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/todos/${todo.id}/`,
          headers: config,
        })
        .then((res) => {
          console.log(res)
          commit('DELETE_TODO', todo)
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    updateTodoStatus: function ({ commit }, { todo, token }) {
      const todoItem = {
        ...todo,  // id, title
        completed: !todo.completed
      }
      const config = { Authorization: `JWT ${token}` }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todoItem,
        headers: config,
      })
        .then((res) => {
          console.log(res.data)
          commit('UPDATE_TODO_STATUS', res.data)
          // todo.completed = !todo.completed
        })
    }
  },
  modules: {
  }
})
