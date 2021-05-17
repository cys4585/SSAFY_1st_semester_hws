import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [],
  },
  mutations: {
    SET_TODOS: function (state, todos) {
      state.todos = todos
    },
    DELETE_TODO: function (state, todoId) {
      state.todos = state.todos.filter(todo => {
        if (todo.id !== todoId) {
          return todo
        }
      })
    },
    UPDATE_TODO_STATUS: function (state, updatedTodo) {
      state.todos = state.todos.map(todo => {
        if (todo.id === updatedTodo.id) {
          return { ...updatedTodo }
        } else { 
          return { ...todo }
        }
      })
    }
  },
  actions: {
    getTodosFromServer: function ({ commit }) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
      })
        .then((res) => {
          commit('SET_TODOS', res.data)
        })
        .catch(err => console.log(err))
    },
    createTodo: function (context, title) {  
      if (title) {
        const todoItem = { title: title, }
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/todos/',
          data: todoItem
        })
          .then(function () { 
            router.push({ name: 'TodoList' }) 
          })
          .catch(err => console.log(err))
        }
    },
    deleteTodo: function ({ commit }, todo) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`
      })
        .then(res => {
          commit('DELETE_TODO', res.data.id)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateTodoStatus: function ({ commit }, todo) {
      const todoItem = {
        ...todo,
        completed: !todo.completed
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todoItem,
      })
        .then((res) => {
          commit('UPDATE_TODO_STATUS', res.data)
        })
        .catch(err => console.log(err))
      },
  },
  modules: {
  }
})
