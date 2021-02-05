<template>
    <div id = "startStu">
       <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container >
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowStu></flowStu>
      </el-aside>
        <el-main>
          <el-row style="margin-bottom:20px">
            <el-col span="8">
            <el-input v-model="title" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col span="6">
              <el-button round @click="addtitle" v-if="isnew">提交题目</el-button>
              <el-button v-else @click="changetitle">更换题目</el-button>
            </el-col>
            <el-col span="6">
              <el-upload v-if="!isnew"
                :data="dataf"
                :headers="headerf"
                name = "work"
     accept=".doc, .docx, .pdf"
      action='/api/uploadfile/'
      :show-file-list="false"
      :on-success="handlefileSuccess"
      :before-upload="beforefileUpload"
      >
      <el-button size="small" type="primary">点击上传</el-button>

</el-upload>
              <span v-if="!isnew"style="margin-left:10px">支持.doc/.docx/.pdf文件</span>
            </el-col>
          </el-row>
<el-collapse >
  <el-collapse-item v-for="(item,index) in list" :title="'第'+ (index+1) +'次提交'">
    <span class="check">{{item.content}}</span>
    <br>
    <el-button size="mini">下载原始文件</el-button>
    <el-button size="mini">下载评阅文件</el-button>
  </el-collapse-item>

</el-collapse>

        </el-main>
      </el-container>
    </el-container>
    </div>
</template>

<script>
  import topNav from '../components/topNav'
import flowStu from '../components/flowStu'

    export default {
        name: "startStu",
      components: {
      topNav,
      flowStu,
    },
      data(){
          return {
      dataf:{},
            headerf:{},
            title:"",
            workid:"",
            watchId:"20",
            list:[
              // {content:"现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；"},
              // {content:"简化流程：设计简洁直观的操作流程清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担"},
              // {content:"太好了"}
            ],
            isnew:""
  }
      },
      created(){

        this.getdata()
      },
    methods: {
          addtitle(){
            this.$http.post('/api/addWorkTitle/',{'stuId':this.watchId,'title':this.title},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.workid = response['workid'];
                      this.isnew = false
                      this.$message({
                      type: 'info',
                      message: '添加成功'
                        });
                    }
                    else{
                      this.$message.error("添加失败")
                    }

              })
          },
      changetitle(){

      },
 beforefileUpload(file) {

    },
  handlefileSuccess(response, file, fileList) {
   // console.log(response);
   // console.log(file.raw);写一条记录
    this.$http.post('/api/addRecordStu/',{'stuId':this.watchId,'workId':this.workid,'path':response['path'],'process':'S'},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.$message({
                      type: 'info',
                      message: '上传成功'
                        });
                      this.list.push({content:"暂无评价"})
                    }
                    else{
                      this.$message.error("添加失败")
                    }

              })

    },
      getdata(){
        //     读取record(list)和title
        // 设置布尔变量，进行修改或新增
            this.$http.post('/api/getRecordTitle/',{'stuId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code'] ==0) {
                      if(res1['title'] == "null"){
                        this.isnew = true;
                      }else{
                        this.isnew = false;
                        this.title = res1['title'];
                        this.workid = res1['workid'];
                      }
                      for (var i = 0;i<res1['rlist'].length;i++){
                        this.list.push({content:res1['rlist'][i]['fields']['content']})
                      }
                      this.dataf['next'] = this.list.length + 1;
                    }
                    else{
                      this.$message.error("获取信息失败")
                    }

              })
      }
    }
    }
</script>

<style scoped>
.check{
  font-size: medium;
}
</style>
