<template >
  <div id = "home">
    <el-container direction="vertical">
      <topNav v-bind:watchId="watchId" v-if="role!=3"></topNav>
      <manageNav  v-if="role==3"></manageNav>
       <el-container>
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowStu v-if="role==1" ></flowStu>
        <flowTea v-if="role==2" ></flowTea>
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
              <el-col>学号</el-col> <el-col>{{item.user.code}}</el-col>
              <el-col>名字</el-col> <el-row>{{item.user.name}}</el-row>
            </el-row>
              <el-row>{{item.title}}</el-row>
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
import flowTea from '../components/flowTea'
import manageNav from '../components/manageNav'
  export default {
    name: 'home',
    components: {
      topNav,
      flowStu,
      flowTea,
      manageNav,
    },
    data() {
      return {
        list:[
            // {user:{code:"17111012",name:"张三"},title:"毕设1",content:"管理系统",},

         ],
        loading: false,
        watchId:'',
        role:0,
        alldata:[],
        count:0,
      }
    },
    mounted: function () {
      this.getCurUserID()
    },
    computed:{
      noMore(){
        return this.count >= this.alldata.length;
      },
      disabled () {
        return this.loading || this.noMore
      }
    },
    methods: {
      load () {
        this.loading = true;
        var i = this.count;
        for (i =this.count;i<this.alldata.length&&i<this.count+3;i++)
        {
          this.list.push({user:{code:this.alldata[i][1],name:this.alldata[i][0]},
          title:this.alldata[i][2],
            content:this.alldata[i][3],
          })
        }
        console.log(this.list);
          this.count = i;
          this.loading = false
      },
      inithome(){
        this.$http.post('/api/initHome/',{'watchId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.alldata = res1["data"];
                    }
                    else{
                      this.$message.error("系统错误")
                    }

              })
      },
      getCurUserID(){
        this.$http.get('/api/getCurUserID')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText)
                  if (res1['err_num'] == 0) {
                    this.watchId = res1['userID'];
                    this.role = res1['role'];
                    this.inithome();
                  }
                })
      }
    }
  }
</script>
