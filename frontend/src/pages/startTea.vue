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
        <el-col span="6"><span>{{item.file}}</span></el-col>
        <el-col span="6"><el-button plain size="small">下载最新提交</el-button></el-col>
      </el-row>
      <el-divider content-position="left">我的评阅</el-divider>
      <el-input
  type="textarea"
  :rows="20"
  placeholder="请输入内容"
  v-model="textarea">
</el-input>
      <el-upload
     accept=".doc, .docx, .pdf"
      action="#"
      :before-upload="beforeAvatarUpload"
      :http-request="getfileUpload"
      :on-change="getValChange"
      :file-list="fileList"
      >
      <el-button size="small" type="primary">点击上传</el-button>
      <span style="margin-left:10px">支持.doc/.docx/.pdf文件</span>
</el-upload>
      <el-divider></el-divider>
      <el-button plain>提交</el-button>
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
            textarea:"",
            list:[
              {code:"171110133",name:"朱振南2",file:"balaa"},
              {code:"171110133",name:"朱振南4",file:"balaa"},
              {code:"171110133",name:"朱振南3",file:"balaa"},
              {code:"171110133",name:"朱振南1",file:"balaa"},
            ],
            currentdata:[],
  }
      },
    methods: {
          fileUpload(data){
    let url = '/card/scrapApply/uploadScrapCards';
    return postResponse(url,data,{contentType:'form'})
 },
      // 上传触发前 对文件格式的校验只校验了excel文件
 beforeAvatarUpload(file) {
      let FileExt = file.name.replace(/.+\./, "").toLowerCase();
      let flag = ["doc", "docx","pdf"].includes(FileExt);
      if (!flag) this.$message.error("只能上传doc\\docx\\pdf文件!");
      return flag;
    },
// 文件值改变时触发 change事件
    getValChange(file, fileList) {
      if (fileList.length > 0) {
        this.fileList = [fileList[fileList.length - 1]]
      }else{
        this.fileList = fileList[0]
      }
    },
  // 上传调用后台接口
  getfileUpload() {
      let formData = new FormData();
      formData.append("file",  this.fileList[0].raw);
      this.fileUpload(formData).then((res) => {
        this.$message.success("上传成功!");
      });
    },
      handleClick(){
            //更改currentuser,上传给不同的人
        this.textarea = "";
      }
    }
    }
</script>

<style scoped>
.check{
  font-size: medium;
}
</style>
