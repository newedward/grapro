<template>
    <div id = "startTea">
       <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container >
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowTea></flowTea>
      </el-aside>
        <el-main>
          <el-row style="margin-bottom:20px">
            <el-tabs   type="card" @tab-click="handleClick">
    <el-tab-pane v-for="item in list" :label="item.name">
      <el-row style="margin: 10px">
        <el-col span="6"><span>{{item.exp}}</span></el-col>
        <el-col span="6"><el-button plain size="small" @click="downloadfile(item.file)">下载最新提交</el-button></el-col>
      </el-row>
      <el-divider content-position="left">我的评阅</el-divider>
      <el-input
  type="textarea"
  :rows="20"
  placeholder="请输入内容"
  v-model="item.com">
</el-input>
      <el-divider></el-divider>
      <el-button plain @click="submitcom">提交</el-button>
    </el-tab-pane>

  </el-tabs>
          </el-row>

        </el-main>
      </el-container>
    </el-container>
    </div>
</template>

<script>
  import topNav from '../components/topNav'
import flowTea from '../components/flowTea'

    export default {
        name: "startTea",
      components: {
      topNav,
      flowTea,
    },
      data(){
          return {
      fileList: [],
            list:[
              // {code:"171110133",name:"朱振南2",file:"balaa",exp:"修改了",com:"szyd"},
              // {code:"171110133",name:"朱振南4",file:"balaa"},
              // {code:"171110133",name:"朱振南3",file:"balaa"},
              // {code:"171110133",name:"朱振南1",file:"balaa"},
            ],
            currentdata:[],
            watchId:"",
            role:'',
  }
      },
      created(){
        this.getCurUserID();
        // this.getstufile();
      },
    methods: {
          getCurUserID(){
        this.$http.get('/api/getCurUserID')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText)
                  if (res1['err_num'] == 0) {
                    this.watchId = res1['userID'];
                    this.role = res1['role'];
                    this.getdata();
                  }
                })
      },
          getdata(){
            this.$http.post('/api/getStudentStartbyTea/',{'teaId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      for (var i = 0; i < res1['ulist'].length; i++) {
                        this.list.push({name:res1['ulist'][i]['fields']['name']
                        ,file:res1['rlist'][i]['fields']['path']}
                        ,)
                      }
                    }
                    else{
                      this.$message.error("获取学生信息失败")
                    }
              })
          },
      downloadfile(path){
            console.log(path);
      },
      handleClick(){}

      },
      submitcom(){

      }
    }

</script>

<style scoped>
.check{
  font-size: medium;
}
</style>
