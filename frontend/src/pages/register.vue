<template>
  <div id="register" >
    <el-row type="flex" justify="center">
      <el-image :src= "require('@/assets/icon.jpg')" fit="fill"></el-image>
    </el-row>
    <el-row type="flex" justify="center">
    <el-col :span="8" type="flex" justify="start">
  <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm" >
    <el-form-item label="姓名" prop="name">
    <el-input placeholder="请输入姓名" v-model="ruleForm.name" autocomplete="off" clearable ></el-input>
  </el-form-item>
    <el-form-item label="用户名" prop="username">
    <el-input placeholder="用户名4到16位（字母，数字，下划线，减号）组成" v-model="ruleForm.username" autocomplete="off" clearable ></el-input>
  </el-form-item>
  <el-form-item label="密码" prop="pass">
    <el-input placeholder="请输入密码" type="password" v-model="ruleForm.pass" autocomplete="off" clearable></el-input>
  </el-form-item>
  <el-form-item label="确认密码" prop="checkPass">
    <el-input placeholder="请重复输入密码" type="password" v-model="ruleForm.checkPass" autocomplete="off" clearable></el-input>
  </el-form-item>
  <el-form-item label="所属学校" prop="uni">
    <el-input placeholder="请输入所属学校" v-model="ruleForm.uni" autocomplete="off" clearable ></el-input>
  </el-form-item>
  <el-form-item label="所属学院" prop="school">
    <el-input placeholder="请输入所属学院" v-model="ruleForm.school" autocomplete="off" clearable ></el-input>
  </el-form-item>
    <el-form-item label="角色" prop="role">
   <el-select  placeholder="请选择" v-model="ruleForm.role">
    <el-option
      v-for="item in ruleForm.options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  </el-form-item>

    <el-form-item label="学号" prop="code" v-show="ruleForm.role=='学生'">
      <el-input placeholder="请输入学号" v-model="ruleForm.code" autocomplete="off" clearable ></el-input>
    </el-form-item>

    <el-form-item label="要求" prop="req" v-show="ruleForm.role=='教师'">
      <el-input placeholder="请输入招生要求（可为空）" v-model="ruleForm.req" autocomplete="off" clearable ></el-input>
    </el-form-item>

    <el-form-item label="电子邮箱" prop="email">
    <el-input placeholder="请输入电子邮箱(非必填)" v-model="ruleForm.email" autocomplete="off" clearable ></el-input>
  </el-form-item>
    <el-form-item label="头像" prop="avater">

      <el-col :span ="10">

    <el-upload
  class="avatar-uploader"
  name = "avater"
     accept=".jpg, .jpeg, .png"
  action='/api/uploadAvater/'
  :show-file-list="false"
  :on-success="handleAvatarSuccess"
  :before-upload="beforeAvatarUpload">
  <img v-if="avater" :src="avater" class="avatar">
  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
</el-upload>
    </el-col>
      </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
  </el-form-item>
  <el-form-item>
    <el-link href="/home" type="primary">回到首页</el-link>
  </el-form-item>
</el-form>
    </el-col>
      </el-row>
  </div>

</template>

<script>

export default {
  name: 'register',
  components: {},
  data() {
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else if (value.length>30){
          callback(new Error('密码长度过长'));
        }
        else {
          if (this.ruleForm.checkPass !== '') {
            this.$refs.ruleForm.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      var validateUsername = (rule, value, callback) => {
        var uPattern = /^[a-zA-Z0-9_-]{4,16}$/;
        if (!uPattern.test(value)) {
          callback(new Error('用户名不合要求'));
        } else {
          this.$http.post('/api/validateUserName/', {'username': value}, {emulateJSON: true})
            .then(function (response) {
              var res1 = JSON.parse(response.bodyText);
              if (res1['err_code'] == 0) {
                callback();
              } else {
                callback(new Error('用户名已存在'));
              }

            })
        }
      };
      var validateName = (rule, value, callback) => {
          if (value.length>20) {
            callback(new Error('姓名长度不能大于20'));
          } else if(value.length<=0)
          {
            callback(new Error('昵称不能为空'));
          }else {
            callback();
          }

      };
      var validateuni = (rule, value, callback) => {
           if(value.length<=0)
          {
            callback(new Error('学校不能为空'));
          }else {
              callback();
            }
      };
      var validateschool = (rule, value, callback) => {
           if(value.length<=0)
          {
            callback(new Error('学院不能为空'));
          }else {
              callback();
            }
      };
      var validatecode = (rule, value, callback) => {
           if(value.length<=0)
          {
            callback(new Error('学号不能为空'));
          }else {
              callback();
            }
      };
      var validatedefault = (rule, value, callback) => {
              callback();
      };
      return {
        res: '',
        avater:'',
        avaterpath:'',
        ruleForm: {
          uni:'',
          role:'学生',
          req:'',
          school:'',
          name:'',
          username:'',
          pass: '',
          checkPass: '',
          email:'',
          code:'请输入学号',
        options: [{
          value: '教师',
          label: '教师'
        }, {
          value: '学生',
          label: '学生'
        }]
        },
        rules: {
          name: [
            { validator: validateName, trigger: 'blur' }
          ],
          uni: [
            { validator: validateuni, trigger: 'blur' }
          ],
          school: [
            { validator: validateschool, trigger: 'blur' }
          ],
          avater: [
            { validator: validatedefault, trigger: 'blur' }
          ],
          email: [
            { validator: validatedefault, trigger: 'blur' }
          ],
          username: [
            { validator: validateUsername, trigger: 'blur' }
          ],
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ],
          code: [
            { validator: validatecode, trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {

            var params = new URLSearchParams();
            params.append('userName', this.ruleForm.username);
            params.append('password', this.ruleForm.pass);
            params.append('name', this.ruleForm.name);
            params.append('email', this.ruleForm.email);
            params.append('avatarpath', this.avaterpath);
            params.append('uni', this.ruleForm.uni);
            params.append('school', this.ruleForm.school);
            params.append('role', this.ruleForm.role);
            params.append('code', this.ruleForm.code);
            params.append('req', this.ruleForm.req);

            this.$axios.post('/api/createUser/', params)
            .then(res => {
              this.res = res
                this.$message({
                  type: 'success',
                  message: res.data
                });
              // window.location.href = "/home";
            }, err => {
              this.$message({
                type: 'info',
                message: '注册失败!\n' + err
              });
            });
          } else {
            console.log('error submit!!');

            this.$message({
                type: 'success',
                message: 'error'
              });
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      handleAvatarSuccess(res, file) {
        this.avater = URL.createObjectURL(file.raw);
        console.log(res);
        if(res['err_code']==0) {
                      this.$message({
                      type: 'info',
                      message: '上传成功'
                        });
                      this.avaterpath = res["path"];
                    }
                    else{
                      this.$message.error("添加失败")
                    }

      },
      beforeAvatarUpload(file) {
        const isLt2M = file.size / 1024 / 1024 < 2;
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isLt2M;
      }
    }

}
</script>

<style>

</style>
