<template >
  <div id = "home">
    <el-container direction="vertical">
      <topNav></topNav>
       <el-container>
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowStu></flowStu>
      </el-aside>

      <el-main style="height: 1000px;">
      <el-scrollbar
            style="height: 100%;">
    <div id = "inflist"
       class="list"
      v-infinite-scroll="load"
      infinite-scroll-disabled="disabled">
      <div id="recommend"  v-for="item in list" :key="item.id">
        <el-row  >
            <el-card shadow="hover">
            <el-row>
              <el-col>id</el-col> <el-col>{{item.id}}</el-col>
              <el-col>名字</el-col> <el-row>{{item.user.name}}</el-row>
            </el-row>
              <el-row>标题</el-row>
              {{item.content}}
            </el-card>
        </el-row>
      </div>
    </div>
    <p v-if="loading">加载中...</p>
    <p v-if="noMore">没有更多了</p>
          </el-scrollbar>
      </el-main>
         </el-container>
    </el-container>
</div>
</template>

<style>
 #recommend{
    margin:8px auto;
   height: 20%;
   width: 70%;
  }
 .el-scrollbar__wrap{
      overflow-x:hidden;
  }
</style>

<script>
import topNav from '../components/topNav'
import flowStu from '../components/flowStu'
  export default {
    name: 'home',
    components: {
      topNav,
      flowStu,
    },
    data() {
      return {
        list:[
            {id:"1",user:{name:"张三"},title:"毕设1",content:"管理系统",},
            {id:"2",user:{name:"张三"},title:"毕设1",content:"管理系统",},
            {id:"3",user:{name:"张三"},title:"毕设1",content:"管理系统",},
            {id:"4",user:{name:"张三"},title:"毕设1",content:"管理系统",},
          {id:"5",user:{name:"张三"},title:"毕设1",content:"管理系统",},
          // {id:"6",user:{name:"张三"},title:"毕设1",content:"管理系统",},
          // {id:"7",user:{name:"张三"},title:"毕设1",content:"管理系统",},
          // {id:"8",user:{name:"张三"},title:"毕设1",content:"管理系统",},
          // {id:"9",user:{name:"张三"},title:"毕设1",content:"管理系统",},
          // {id:"10",user:{name:"张三"},title:"毕设1",content:"管理系统",},
          // {id:"11",user:{name:"张三"},title:"毕设1",content:"管理系统",},
          // {id:"12",user:{name:"张三"},title:"毕设1",content:"管理系统",},
         ],
        loading: false
      }
    },
    computed:{
      noMore () {
        return this.list.length >= 14
      },
      disabled () {
        return this.loading || this.noMore
      }
    },
    methods: {
      load () {
        this.loading = true
        setTimeout(() => {
          this.list.push({id:this.list.length+1,user:{name:"张三"},title:"毕设1",content:"管理系统",})
          this.loading = false
        }, 1000)
      }
    }
  }
</script>
