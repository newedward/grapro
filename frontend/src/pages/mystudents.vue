<template>
    <div id = "mystudents">
       <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container >
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowTea></flowTea>
      </el-aside>
        <el-main>
          <el-row type="flex" justify="center">
            <span class="title">等待队列</span>
            <el-button @click="store">保存</el-button>
          </el-row>
          <el-row>
<draggable  v-model="groups" @chang="change" @start="start" @end="end" :move="move">
    <el-card v-for="item in groups" :key=index class="stu">
      <el-avatar shape="circle" :src="item.avater"></el-avatar>
      <span >{{item.code + "-" + item.name + item.uid}}</span>
      <el-button style="float: right" icon="el-icon-close" @click="delqueue(index)">移除</el-button>
    </el-card>
</draggable>
          </el-row>
          <el-divider></el-divider>
          <el-row type="flex" justify="center">
            <span class="title">我的学生</span>
          </el-row>
          <el-row type="flex" justify="center" v-for="rows in branch">
            <el-card class="student" v-for="cols in rows">

              <el-avatar :size="40" shape="circle" :src="cols.avater"></el-avatar>
              <span class="intro">{{cols.code + cols.name}}</span>
        </el-card>
          </el-row>
        </el-main>
      </el-container>

    </el-container>
    </div>
</template>

<script>
  import topNav from '../components/topNav'
import flowTea from '../components/flowTea'
  import draggable from 'vuedraggable'
    export default {
        name: "mystudents",
      components: {
      topNav,
      flowTea,
        draggable,
    },
      data(){
           return {
             groups: [
        // {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"张三",intro:"不忘初心"},
        //     {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"陈斌",intro:"不忘初心"},
        //     {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"马化腾",intro:"不忘初心"},
        //     {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"李四",intro:"不忘初心"},
        //   {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"马云",intro:"不忘初心"},
        //      {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"马云",intro:"不忘初心"},
      ],
             queue:[],
             rownumber:5,
             watchId:'',
             role:'',
           list: [
          //    {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110134",name:"朱振南",intro:"不忘初心"},
          //   {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110135",name:"朱振南",intro:"不忘初心"},
          //   {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110133",name:"朱振南",intro:"不忘初心"},
          //   {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110132",name:"朱振南",intro:"不忘初心"},
          // {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110131",name:"朱振南",intro:"不忘初心"},
          //    {avater:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",code:"171110130",name:"朱振南",intro:"不忘初心"},
           ],
             branch:[],
    }
      },
      mounted() {
          this.getCurUserID();

      },
      methods:{
          change (event) {
      console.log('change', event)
    },
    start (event) {
      console.log('start', event)
    },
    end (event) {
      console.log('end', event, this.groups)
    },
    move (event, origin) {
      console.log('move', event, origin)
    },
        getRow () {
        let arr = [];
        let row = Math.ceil(this.list.length / this.rownumber);
        for (let i = 0; i < row; i++) {
          arr[i] = [];
          let modLast = this.list.length % this.rownumber === 0 ? this.rownumber : this.list.length % this.rownumber;
           let lastRow = i === (row - 1) ? modLast : this.rownumber;
          for (let j = 0; j < lastRow; j++) {
                 arr[i][j] = this.list[this.rownumber * i + j];
          }
         }
        this.branch = arr;
       },
        getdata(){
            this.$http.post('/api/getTeaQueue/',{'teacherId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      for (var i = 0; i < res1['ulist'].length; i++) {
                        this.groups.push({avater:res1['ulist'][i]['fields']['avater']
                        ,name:res1['ulist'][i]['fields']['name'],intro:"一期测试"
                        ,uid:res1['ulist'][i]['pk'],code:res1['slist'][i]['fields']['code']
                        })
                        //uid指的是学生的id
                      }
                    }
                    else{
                      this.$message.error("获取队列信息失败")
                    }
              })
        },
        delqueue(val){
            this.queue.splice(val,1);
        },
        getCurUserID(){
        this.$http.get('/api/getCurUserID')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText)
                  if (res1['err_num'] == 0) {
                    this.watchId = res1['userID'];
                    this.role = res1['role'];
                    this.getdata();
                    this.getlist();
                  }
                })
      },
        store(){
            for (var i=0;i<this.groups.length;i++){
              this.queue.push(this.groups[i].uid)
            }
            console.log(this.queue);
            var conque = this.queue
            this.queue = [];
            this.$http.post('/api/storeTeaQueue/',{'queue':JSON.stringify(conque),'teaid':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.$message({
                      type: 'info',
                      message: '保存成功'
                        });

                    }
                    else{
                      this.$message.error("保存失败")
                    }

              })
        },
        getlist(){
            this.$http.post('/api/getMyStudent/',{'teacherId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {

                      for (var i = 0; i < res1['slist'].length; i++) {
                        this.list.push({avater:res1['ulist'][i]['fields']['avater']
                        ,name:res1['ulist'][i]['fields']['name'],code:res1['slist'][i]['fields']['code']
                        ,uid:res1['slist'][i]['pk']})
                      }
                      this.getRow();
                    }
                    else{
                      this.$message.error("获取我的学生信息失败")
                    }
              })
        }
      }
    }
</script>

<style scoped>
.title{
    font-weight:bold;
	color: #57acff;
  }
  .stu{
    margin: 10px;
  }
  .student{
    margin: 6px;
  }
</style>
